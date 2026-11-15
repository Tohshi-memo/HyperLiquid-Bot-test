# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T03:52:28.714734+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.52` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.4649` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.0153` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0127` n `13`; crypto_alt avg `-0.2823` n `239`; crypto_major avg `-0.3484` n `8`; equity avg `-0.0194` n `162`; fx avg `0.0067` n `6`; index avg `-0.0087` n `27`; metal avg `-0.0506` n `20`; unknown avg `0.4064` n `1261`
- 1h: commodity avg `-0.007` n `13`; crypto_alt avg `0.2324` n `239`; crypto_major avg `0.3927` n `8`; equity avg `0.1111` n `162`; fx avg `-0.004` n `6`; index avg `-0.0039` n `27`; metal avg `-0.0101` n `20`; unknown avg `0.0776` n `1259`
- 4h: commodity avg `0.0263` n `13`; crypto_alt avg `1.814` n `239`; crypto_major avg `2.4912` n `8`; equity avg `0.4759` n `162`; fx avg `0.01` n `6`; index avg `-0.0014` n `27`; metal avg `-0.0288` n `20`; unknown avg `1.6718` n `1248`
- 24h: commodity avg `0.0294` n `13`; crypto_alt avg `-5.247` n `239`; crypto_major avg `-3.4339` n `8`; equity avg `-0.5991` n `162`; fx avg `0.0433` n `6`; index avg `-0.065` n `27`; metal avg `-0.4096` n `20`; unknown avg `48.1486` n `1068`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1409`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.116`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1156`, n `669`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1141`, n `669`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1103`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0886`, n `669`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0832`, n `669`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0828`, n `669`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.082`, n `669`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0807`, n `669`, weak_sample_signal
