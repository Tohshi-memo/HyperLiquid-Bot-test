# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T20:22:30.577447+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0079` n `12`; crypto_alt avg `0.028` n `234`; crypto_major avg `-0.1362` n `8`; equity avg `-0.0102` n `140`; fx avg `-0.0078` n `6`; index avg `-0.0049` n `26`; metal avg `-0.0074` n `20`; unknown avg `8.3714` n `943`
- 1h: commodity avg `-0.0057` n `12`; crypto_alt avg `0.6293` n `234`; crypto_major avg `0.1482` n `8`; equity avg `0.0378` n `140`; fx avg `0.0128` n `6`; index avg `-0.0092` n `26`; metal avg `-0.0077` n `20`; unknown avg `17.7051` n `935`
- 4h: commodity avg `0.0147` n `12`; crypto_alt avg `1.4899` n `234`; crypto_major avg `0.6706` n `8`; equity avg `0.0673` n `140`; fx avg `-0.0226` n `6`; index avg `-0.0029` n `26`; metal avg `-0.022` n `20`; unknown avg `14.0506` n `915`
- 24h: commodity avg `0.372` n `12`; crypto_alt avg `0.5233` n `234`; crypto_major avg `-0.4161` n `8`; equity avg `-0.1068` n `140`; fx avg `-0.005` n `6`; index avg `-0.0496` n `26`; metal avg `-0.046` n `20`; unknown avg `3.9833` n `827`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1616`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1456`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
