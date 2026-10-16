# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T18:27:54.855858+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.5384` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.3159` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0661` n `13`; crypto_alt avg `0.0729` n `236`; crypto_major avg `0.1131` n `8`; equity avg `-0.1709` n `151`; fx avg `0.0033` n `6`; index avg `-0.0366` n `26`; metal avg `-0.0383` n `20`; unknown avg `25.6035` n `1177`
- 1h: commodity avg `0.1848` n `13`; crypto_alt avg `0.6654` n `236`; crypto_major avg `0.7495` n `8`; equity avg `-0.0806` n `151`; fx avg `-0.0009` n `6`; index avg `-0.0197` n `26`; metal avg `-0.0241` n `20`; unknown avg `206.2721` n `1175`
- 4h: commodity avg `0.8224` n `13`; crypto_alt avg `-2.183` n `236`; crypto_major avg `-1.716` n `8`; equity avg `-2.0068` n `151`; fx avg `-0.0467` n `6`; index avg `-0.4001` n `26`; metal avg `-0.3125` n `20`; unknown avg `4.721` n `1056`
- 24h: commodity avg `0.2293` n `13`; crypto_alt avg `-1.5831` n `236`; crypto_major avg `-1.3071` n `8`; equity avg `-2.3292` n `151`; fx avg `-0.0054` n `6`; index avg `-0.4603` n `26`; metal avg `-0.0535` n `20`; unknown avg `-0.6111` n `904`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1495`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1042`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0989`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0789`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0788`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0727`, n `666`, weak_sample_signal
