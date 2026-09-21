# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T18:07:31.004133+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0146` n `12`; crypto_alt avg `0.3847` n `234`; crypto_major avg `0.3536` n `8`; equity avg `0.0745` n `140`; fx avg `-0.0001` n `6`; index avg `0.0081` n `26`; metal avg `0.0451` n `20`; unknown avg `-0.0445` n `940`
- 1h: commodity avg `0.1315` n `12`; crypto_alt avg `-0.5121` n `234`; crypto_major avg `-0.0317` n `8`; equity avg `0.1289` n `140`; fx avg `-0.001` n `6`; index avg `0.0315` n `26`; metal avg `0.0308` n `20`; unknown avg `-0.2299` n `940`
- 4h: commodity avg `-0.0556` n `12`; crypto_alt avg `0.1027` n `234`; crypto_major avg `1.0693` n `8`; equity avg `0.8711` n `140`; fx avg `-0.0049` n `6`; index avg `0.236` n `26`; metal avg `-0.0266` n `20`; unknown avg `0.5564` n `892`
- 24h: commodity avg `-0.964` n `12`; crypto_alt avg `3.6145` n `234`; crypto_major avg `5.2216` n `8`; equity avg `2.8074` n `140`; fx avg `-0.0885` n `6`; index avg `0.6058` n `26`; metal avg `0.0161` n `20`; unknown avg `6.7008` n `739`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.184`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1628`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1334`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
