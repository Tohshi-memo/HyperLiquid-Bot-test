# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T19:07:30.129653+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0114` n `12`; crypto_alt avg `0.1963` n `234`; crypto_major avg `0.1881` n `8`; equity avg `0.0532` n `140`; fx avg `-0.0002` n `6`; index avg `0.0015` n `26`; metal avg `0.0241` n `20`; unknown avg `1.1441` n `940`
- 1h: commodity avg `0.234` n `12`; crypto_alt avg `0.1653` n `234`; crypto_major avg `0.3687` n `8`; equity avg `0.0514` n `140`; fx avg `0.0207` n `6`; index avg `-0.009` n `26`; metal avg `0.0593` n `20`; unknown avg `1.5256` n `940`
- 4h: commodity avg `0.017` n `12`; crypto_alt avg `1.1448` n `234`; crypto_major avg `0.5933` n `8`; equity avg `0.522` n `140`; fx avg `0.0188` n `6`; index avg `0.064` n `26`; metal avg `0.2789` n `20`; unknown avg `1.5076` n `880`
- 24h: commodity avg `0.1461` n `12`; crypto_alt avg `2.5664` n `234`; crypto_major avg `1.4051` n `8`; equity avg `0.6942` n `140`; fx avg `-0.2783` n `6`; index avg `0.0839` n `26`; metal avg `0.2775` n `20`; unknown avg `1.0324` n `796`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
