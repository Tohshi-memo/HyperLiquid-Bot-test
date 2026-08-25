# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T12:18:50.858041+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.8132` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.5198` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0432` n `12`; crypto_alt avg `0.2439` n `231`; crypto_major avg `0.1995` n `8`; equity avg `0.0899` n `122`; fx avg `0.0054` n `6`; index avg `0.0179` n `25`; metal avg `-0.0107` n `20`; unknown avg `0.1136` n `795`
- 1h: commodity avg `-0.1609` n `12`; crypto_alt avg `-0.3778` n `231`; crypto_major avg `-0.3512` n `8`; equity avg `0.0993` n `122`; fx avg `-0.0118` n `6`; index avg `0.0426` n `25`; metal avg `-0.0324` n `20`; unknown avg `-0.0511` n `795`
- 4h: commodity avg `-0.4671` n `12`; crypto_alt avg `-1.0452` n `231`; crypto_major avg `-1.3867` n `8`; equity avg `0.4265` n `122`; fx avg `-0.0506` n `6`; index avg `0.1331` n `25`; metal avg `-0.0046` n `20`; unknown avg `0.0401` n `794`
- 24h: commodity avg `-0.9057` n `12`; crypto_alt avg `-0.6922` n `231`; crypto_major avg `-0.2064` n `8`; equity avg `0.6563` n `122`; fx avg `0.0186` n `6`; index avg `0.152` n `25`; metal avg `-0.3011` n `20`; unknown avg `-0.2838` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
