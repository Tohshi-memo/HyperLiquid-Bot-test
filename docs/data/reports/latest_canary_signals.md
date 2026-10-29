# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T22:22:26.324493+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-3.0344` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-3.0045` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.7964` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0074` n `13`; crypto_alt avg `0.9545` n `238`; crypto_major avg `0.5721` n `8`; equity avg `-0.0716` n `156`; fx avg `0.0111` n `6`; index avg `-0.0175` n `27`; metal avg `-0.0142` n `20`; unknown avg `0.3362` n `1260`
- 1h: commodity avg `0.0196` n `13`; crypto_alt avg `-0.8611` n `238`; crypto_major avg `-0.3882` n `8`; equity avg `-0.1682` n `156`; fx avg `0.0104` n `6`; index avg `-0.0135` n `27`; metal avg `0.022` n `20`; unknown avg `0.327` n `1252`
- 4h: commodity avg `0.0319` n `13`; crypto_alt avg `-4.6452` n `238`; crypto_major avg `-2.9726` n `8`; equity avg `-2.4146` n `156`; fx avg `0.0292` n `6`; index avg `-0.1762` n `27`; metal avg `0.0618` n `20`; unknown avg `22.7457` n `1162`
- 24h: commodity avg `-0.2069` n `13`; crypto_alt avg `-5.5109` n `238`; crypto_major avg `-1.7203` n `8`; equity avg `-3.3208` n `155`; fx avg `0.0659` n `6`; index avg `-0.2615` n `27`; metal avg `-0.5687` n `20`; unknown avg `29.5784` n `976`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
