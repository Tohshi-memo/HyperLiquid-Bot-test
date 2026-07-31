# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T14:22:38.251405+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.9779` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_equity_divergence: score `1.5189` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0068` n `12`; crypto_alt avg `0.5751` n `230`; crypto_major avg `0.4618` n `8`; equity avg `0.3023` n `102`; fx avg `0.0496` n `6`; index avg `0.0533` n `25`; metal avg `0.1031` n `20`; unknown avg `0.6628` n `780`
- 1h: commodity avg `-0.099` n `12`; crypto_alt avg `-0.4414` n `230`; crypto_major avg `-0.7537` n `8`; equity avg `-2.2726` n `102`; fx avg `-0.1135` n `6`; index avg `-0.3293` n `25`; metal avg `-0.0952` n `20`; unknown avg `0.0245` n `780`
- 4h: commodity avg `0.0984` n `12`; crypto_alt avg `-0.2356` n `230`; crypto_major avg `-0.412` n `8`; equity avg `-2.3899` n `102`; fx avg `-0.147` n `6`; index avg `-0.3871` n `25`; metal avg `-0.2239` n `20`; unknown avg `1.2623` n `780`
- 24h: commodity avg `0.3065` n `12`; crypto_alt avg `-1.0032` n `230`; crypto_major avg `-1.1102` n `8`; equity avg `0.0852` n `102`; fx avg `0.115` n `6`; index avg `0.1611` n `25`; metal avg `-0.2575` n `20`; unknown avg `1.4476` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
