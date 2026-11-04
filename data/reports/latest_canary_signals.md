# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T03:37:25.420950+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.38` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-1.894` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5304` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0218` n `13`; crypto_alt avg `0.1132` n `239`; crypto_major avg `0.2141` n `8`; equity avg `-0.1924` n `158`; fx avg `0.0004` n `6`; index avg `-0.0232` n `27`; metal avg `-0.057` n `20`; unknown avg `0.2436` n `1264`
- 1h: commodity avg `0.0793` n `13`; crypto_alt avg `-0.3741` n `239`; crypto_major avg `-0.1894` n `8`; equity avg `-0.4634` n `158`; fx avg `0.008` n `6`; index avg `-0.0279` n `27`; metal avg `-0.1533` n `20`; unknown avg `1.4704` n `1256`
- 4h: commodity avg `-0.2848` n `13`; crypto_alt avg `-2.3187` n `239`; crypto_major avg `-2.1684` n `8`; equity avg `-3.6283` n `158`; fx avg `-0.0576` n `6`; index avg `-0.638` n `27`; metal avg `-0.2744` n `20`; unknown avg `9.1387` n `1252`
- 24h: commodity avg `-0.1558` n `13`; crypto_alt avg `-0.0098` n `239`; crypto_major avg `-0.3084` n `8`; equity avg `-1.1165` n `158`; fx avg `0.1155` n `6`; index avg `-0.4032` n `27`; metal avg `-0.4868` n `20`; unknown avg `-0.3557` n `1009`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
