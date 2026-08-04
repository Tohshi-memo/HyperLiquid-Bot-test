# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T15:37:34.511020+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.542` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.085` n `12`; crypto_alt avg `-0.1483` n `230`; crypto_major avg `-0.2304` n `8`; equity avg `0.0625` n `107`; fx avg `-0.003` n `6`; index avg `0.0191` n `25`; metal avg `0.0109` n `20`; unknown avg `-0.0504` n `782`
- 1h: commodity avg `-0.108` n `12`; crypto_alt avg `-0.0989` n `230`; crypto_major avg `-0.1235` n `8`; equity avg `0.6899` n `107`; fx avg `-0.0101` n `6`; index avg `0.1096` n `25`; metal avg `0.0693` n `20`; unknown avg `-0.0632` n `782`
- 4h: commodity avg `-0.9414` n `12`; crypto_alt avg `-0.406` n `230`; crypto_major avg `-0.0986` n `8`; equity avg `1.4434` n `107`; fx avg `-0.021` n `6`; index avg `0.366` n `25`; metal avg `0.2597` n `20`; unknown avg `-0.3204` n `781`
- 24h: commodity avg `-1.0437` n `12`; crypto_alt avg `-0.472` n `230`; crypto_major avg `-0.0228` n `8`; equity avg `4.403` n `107`; fx avg `0.0836` n `6`; index avg `0.8008` n `25`; metal avg `1.0612` n `20`; unknown avg `0.4535` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1475`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1424`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
