# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T18:37:33.736583+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.6308` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.3592` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0219` n `13`; crypto_alt avg `-0.1241` n `236`; crypto_major avg `-0.0514` n `8`; equity avg `-0.0217` n `151`; fx avg `-0.0009` n `6`; index avg `0.0004` n `26`; metal avg `-0.005` n `20`; unknown avg `4.1137` n `1177`
- 1h: commodity avg `-0.0294` n `13`; crypto_alt avg `-0.283` n `236`; crypto_major avg `-0.0974` n `8`; equity avg `-0.4532` n `151`; fx avg `-0.0069` n `6`; index avg `-0.0963` n `26`; metal avg `-0.0446` n `20`; unknown avg `238.0747` n `1175`
- 4h: commodity avg `0.8448` n `13`; crypto_alt avg `-2.3119` n `236`; crypto_major avg `-1.786` n `8`; equity avg `-2.1703` n `151`; fx avg `-0.0485` n `6`; index avg `-0.4268` n `26`; metal avg `-0.3044` n `20`; unknown avg `7.3649` n `1064`
- 24h: commodity avg `0.2927` n `13`; crypto_alt avg `-1.9502` n `236`; crypto_major avg `-1.5736` n `8`; equity avg `-2.5443` n `151`; fx avg `-0.0089` n `6`; index avg `-0.4872` n `26`; metal avg `-0.0681` n `20`; unknown avg `3.3392` n `904`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1531`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1073`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1008`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0823`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0764`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0716`, n `666`, weak_sample_signal
