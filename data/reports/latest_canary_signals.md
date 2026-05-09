# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T02:22:16.734578+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0803` n `12`; crypto_alt avg `0.1022` n `228`; crypto_major avg `-0.066` n `8`; equity avg `-0.0132` n `65`; fx avg `0.0059` n `5`; index avg `0.0039` n `23`; metal avg `0.0102` n `18`; unknown avg `0.0322` n `375`
- 1h: commodity avg `0.1143` n `12`; crypto_alt avg `0.3655` n `228`; crypto_major avg `0.3786` n `8`; equity avg `-0.0161` n `65`; fx avg `0.0263` n `5`; index avg `0.1143` n `23`; metal avg `0.0728` n `18`; unknown avg `0.3293` n `375`
- 4h: commodity avg `0.0974` n `12`; crypto_alt avg `1.1423` n `228`; crypto_major avg `0.6583` n `8`; equity avg `0.0489` n `65`; fx avg `0.0057` n `5`; index avg `0.1148` n `23`; metal avg `-0.0134` n `18`; unknown avg `0.0192` n `375`
- 24h: commodity avg `-0.3861` n `12`; crypto_alt avg `5.3644` n `228`; crypto_major avg `3.0379` n `8`; equity avg `3.7855` n `65`; fx avg `0.1102` n `5`; index avg `1.4364` n `23`; metal avg `0.3043` n `18`; unknown avg `1.2766` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
