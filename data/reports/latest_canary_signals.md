# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T10:07:29.509430+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.8269` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.319` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0311` n `12`; crypto_alt avg `-0.4798` n `231`; crypto_major avg `-0.5301` n `8`; equity avg `-0.0742` n `127`; fx avg `-0.008` n `6`; index avg `-0.0125` n `26`; metal avg `-0.0032` n `20`; unknown avg `-0.0464` n `792`
- 1h: commodity avg `-0.0449` n `12`; crypto_alt avg `-0.5784` n `231`; crypto_major avg `-0.8101` n `8`; equity avg `-0.1055` n `127`; fx avg `-0.0077` n `6`; index avg `-0.009` n `26`; metal avg `0.0947` n `20`; unknown avg `-0.0416` n `792`
- 4h: commodity avg `-0.0726` n `12`; crypto_alt avg `-0.8799` n `231`; crypto_major avg `-1.3123` n `8`; equity avg `-0.1784` n `127`; fx avg `-0.0215` n `6`; index avg `0.0067` n `26`; metal avg `0.5146` n `20`; unknown avg `-0.0286` n `792`
- 24h: commodity avg `0.1507` n `12`; crypto_alt avg `-1.7927` n `231`; crypto_major avg `-1.5784` n `8`; equity avg `-1.2513` n `127`; fx avg `-0.099` n `6`; index avg `-0.0216` n `26`; metal avg `0.8255` n `20`; unknown avg `0.211` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
