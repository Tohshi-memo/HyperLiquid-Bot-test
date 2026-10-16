# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T18:22:31.474740+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.4823` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.3032` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0238` n `13`; crypto_alt avg `0.0673` n `236`; crypto_major avg `0.1259` n `8`; equity avg `-0.1632` n `151`; fx avg `0.0008` n `6`; index avg `-0.0369` n `26`; metal avg `-0.0367` n `20`; unknown avg `0.029` n `1177`
- 1h: commodity avg `0.1424` n `13`; crypto_alt avg `0.6597` n `236`; crypto_major avg `0.7624` n `8`; equity avg `-0.0728` n `151`; fx avg `-0.0034` n `6`; index avg `-0.0201` n `26`; metal avg `-0.0225` n `20`; unknown avg `196.8228` n `1175`
- 4h: commodity avg `0.7787` n `13`; crypto_alt avg `-2.1886` n `236`; crypto_major avg `-1.7036` n `8`; equity avg `-2.0002` n `151`; fx avg `-0.0492` n `6`; index avg `-0.4004` n `26`; metal avg `-0.3109` n `20`; unknown avg `4.7908` n `1056`
- 24h: commodity avg `0.1857` n `13`; crypto_alt avg `-1.5885` n `236`; crypto_major avg `-1.2948` n `8`; equity avg `-2.3216` n `151`; fx avg `-0.008` n `6`; index avg `-0.4606` n `26`; metal avg `-0.052` n `20`; unknown avg `-0.5826` n `904`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1495`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1039`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0989`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0789`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0781`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0725`, n `666`, weak_sample_signal
