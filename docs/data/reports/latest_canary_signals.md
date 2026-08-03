# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T18:07:31.554805+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.8554` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0615` n `12`; crypto_alt avg `0.1211` n `230`; crypto_major avg `0.0665` n `8`; equity avg `0.2703` n `103`; fx avg `-0.0085` n `6`; index avg `0.0394` n `25`; metal avg `0.0172` n `20`; unknown avg `-0.0276` n `784`
- 1h: commodity avg `-0.0551` n `12`; crypto_alt avg `0.1644` n `230`; crypto_major avg `0.1322` n `8`; equity avg `0.8501` n `103`; fx avg `-0.0162` n `6`; index avg `0.1418` n `25`; metal avg `0.0207` n `20`; unknown avg `-0.0183` n `784`
- 4h: commodity avg `0.1146` n `12`; crypto_alt avg `0.435` n `230`; crypto_major avg `0.8185` n `8`; equity avg `2.6739` n `103`; fx avg `0.0001` n `6`; index avg `0.3883` n `25`; metal avg `0.1099` n `20`; unknown avg `-0.2455` n `784`
- 24h: commodity avg `-0.1262` n `12`; crypto_alt avg `0.3952` n `230`; crypto_major avg `0.863` n `8`; equity avg `2.199` n `102`; fx avg `-0.199` n `6`; index avg `0.1101` n `25`; metal avg `-0.4852` n `20`; unknown avg `0.1563` n `766`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
