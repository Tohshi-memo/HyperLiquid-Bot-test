# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T16:37:53.919508+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.8697` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0673` n `12`; crypto_alt avg `-0.0265` n `230`; crypto_major avg `-0.0987` n `8`; equity avg `-0.0732` n `107`; fx avg `0.0117` n `6`; index avg `0.0052` n `25`; metal avg `0.0313` n `20`; unknown avg `0.0002` n `782`
- 1h: commodity avg `0.0124` n `12`; crypto_alt avg `0.3522` n `230`; crypto_major avg `0.2337` n `8`; equity avg `0.3093` n `107`; fx avg `0.0207` n `6`; index avg `0.0531` n `25`; metal avg `0.1216` n `20`; unknown avg `-0.0044` n `782`
- 4h: commodity avg `-0.4898` n `12`; crypto_alt avg `-0.1806` n `230`; crypto_major avg `-0.2026` n `8`; equity avg `1.6671` n `107`; fx avg `0.0122` n `6`; index avg `0.3967` n `25`; metal avg `0.09` n `20`; unknown avg `-0.2065` n `781`
- 24h: commodity avg `-1.0804` n `12`; crypto_alt avg `-0.1742` n `230`; crypto_major avg `0.1223` n `8`; equity avg `4.2749` n `107`; fx avg `0.0836` n `6`; index avg `0.8023` n `25`; metal avg `1.1098` n `20`; unknown avg `0.4057` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
