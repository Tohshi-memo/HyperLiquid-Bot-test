# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T06:37:28.581033+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0153` n `12`; crypto_alt avg `-0.0467` n `230`; crypto_major avg `0.0196` n `8`; equity avg `0.182` n `112`; fx avg `-0.028` n `6`; index avg `0.0101` n `25`; metal avg `0.0382` n `20`; unknown avg `-0.0152` n `782`
- 1h: commodity avg `-0.0439` n `12`; crypto_alt avg `0.3647` n `230`; crypto_major avg `0.4873` n `8`; equity avg `0.2891` n `112`; fx avg `-0.0266` n `6`; index avg `0.0318` n `25`; metal avg `0.2123` n `20`; unknown avg `0.0243` n `766`
- 4h: commodity avg `0.0523` n `12`; crypto_alt avg `-0.0213` n `230`; crypto_major avg `0.0077` n `8`; equity avg `0.5513` n `112`; fx avg `-0.0256` n `6`; index avg `0.0928` n `25`; metal avg `0.3304` n `20`; unknown avg `-0.033` n `766`
- 24h: commodity avg `0.4783` n `12`; crypto_alt avg `0.2622` n `230`; crypto_major avg `-0.9244` n `8`; equity avg `1.4031` n `109`; fx avg `-0.0641` n `6`; index avg `-0.0251` n `25`; metal avg `0.347` n `20`; unknown avg `110.7944` n `765`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
