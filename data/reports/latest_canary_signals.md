# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T09:22:29.622394+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0588` n `13`; crypto_alt avg `-0.0233` n `234`; crypto_major avg `0.0753` n `8`; equity avg `0.0979` n `142`; fx avg `-0.0037` n `6`; index avg `0.0109` n `26`; metal avg `0.0244` n `20`; unknown avg `0.1184` n `975`
- 1h: commodity avg `-0.0947` n `13`; crypto_alt avg `0.2272` n `234`; crypto_major avg `0.3744` n `8`; equity avg `0.2729` n `142`; fx avg `-0.0202` n `6`; index avg `0.0789` n `26`; metal avg `0.0288` n `20`; unknown avg `0.2248` n `973`
- 4h: commodity avg `0.3518` n `13`; crypto_alt avg `-0.9057` n `234`; crypto_major avg `-0.6495` n `8`; equity avg `-0.5088` n `142`; fx avg `-0.0226` n `6`; index avg `-0.1599` n `26`; metal avg `-0.3832` n `20`; unknown avg `3.7785` n `930`
- 24h: commodity avg `-0.0746` n `13`; crypto_alt avg `-0.0966` n `234`; crypto_major avg `0.5225` n `8`; equity avg `0.4148` n `142`; fx avg `0.0995` n `6`; index avg `0.1078` n `26`; metal avg `-0.3514` n `20`; unknown avg `775.895` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1698`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1344`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
