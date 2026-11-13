# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T05:22:27.955783+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.5631` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-2.4902` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.3792` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0322` n `13`; crypto_alt avg `0.7327` n `239`; crypto_major avg `0.7481` n `8`; equity avg `-0.0853` n `162`; fx avg `0.0132` n `6`; index avg `-0.0263` n `27`; metal avg `0.0067` n `20`; unknown avg `0.5517` n `1260`
- 1h: commodity avg `-0.0381` n `13`; crypto_alt avg `0.1465` n `239`; crypto_major avg `0.2067` n `8`; equity avg `-0.2027` n `162`; fx avg `0.0136` n `6`; index avg `-0.0246` n `27`; metal avg `0.0009` n `20`; unknown avg `44.2792` n `1260`
- 4h: commodity avg `-0.107` n `13`; crypto_alt avg `-2.2604` n `239`; crypto_major avg `-2.5972` n `8`; equity avg `-1.8997` n `162`; fx avg `0.034` n `6`; index avg `-0.218` n `27`; metal avg `-0.0341` n `20`; unknown avg `1.4431` n `1246`
- 24h: commodity avg `0.7945` n `13`; crypto_alt avg `-2.5129` n `239`; crypto_major avg `-3.7705` n `8`; equity avg `-1.0017` n `162`; fx avg `0.0327` n `6`; index avg `0.0234` n `27`; metal avg `-0.3741` n `20`; unknown avg `99.4147` n `1123`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1744`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
