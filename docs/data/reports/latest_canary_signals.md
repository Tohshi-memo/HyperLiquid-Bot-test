# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T20:37:29.683119+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1325` n `13`; crypto_alt avg `-0.3167` n `239`; crypto_major avg `-0.2089` n `8`; equity avg `-0.0345` n `160`; fx avg `-0.0043` n `6`; index avg `0.0078` n `27`; metal avg `0.0037` n `20`; unknown avg `5.4001` n `1261`
- 1h: commodity avg `-0.039` n `13`; crypto_alt avg `-0.0644` n `239`; crypto_major avg `0.1649` n `8`; equity avg `0.6434` n `160`; fx avg `-0.0138` n `6`; index avg `0.0792` n `27`; metal avg `0.1966` n `20`; unknown avg `5.1775` n `1245`
- 4h: commodity avg `-0.1059` n `13`; crypto_alt avg `-0.3362` n `239`; crypto_major avg `-0.241` n `8`; equity avg `0.8456` n `160`; fx avg `-0.0253` n `6`; index avg `0.1625` n `27`; metal avg `0.2859` n `20`; unknown avg `3.2216` n `1245`
- 24h: commodity avg `-0.3517` n `13`; crypto_alt avg `0.5104` n `239`; crypto_major avg `-2.3846` n `8`; equity avg `4.51` n `160`; fx avg `-0.1668` n `6`; index avg `0.5793` n `27`; metal avg `0.7115` n `20`; unknown avg `8.7289` n `1076`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
