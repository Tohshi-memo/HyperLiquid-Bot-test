# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T02:37:26.868795+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.1498` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0558` n `13`; crypto_alt avg `-0.0148` n `239`; crypto_major avg `-0.0536` n `8`; equity avg `0.2045` n `166`; fx avg `-0.0175` n `6`; index avg `0.0318` n `27`; metal avg `-0.0415` n `20`; unknown avg `315.946` n `1266`
- 1h: commodity avg `-0.096` n `13`; crypto_alt avg `-0.691` n `239`; crypto_major avg `-1.1782` n `8`; equity avg `-0.5555` n `166`; fx avg `-0.0422` n `6`; index avg `-0.0284` n `27`; metal avg `-0.273` n `20`; unknown avg `160.1852` n `1264`
- 4h: commodity avg `-0.1396` n `13`; crypto_alt avg `0.6449` n `239`; crypto_major avg `-0.2527` n `8`; equity avg `-0.3447` n `166`; fx avg `0.0261` n `6`; index avg `0.0785` n `27`; metal avg `-0.0219` n `20`; unknown avg `0.841` n `1250`
- 24h: commodity avg `-1.2321` n `13`; crypto_alt avg `1.6726` n `239`; crypto_major avg `1.3006` n `8`; equity avg `6.5546` n `166`; fx avg `-0.2402` n `6`; index avg `0.7468` n `27`; metal avg `0.5952` n `20`; unknown avg `97.8528` n `1049`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
