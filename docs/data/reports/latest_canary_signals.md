# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T02:07:24.155588+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1069` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.9643` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.9619` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0765` n `12`; crypto_alt avg `-0.0183` n `231`; crypto_major avg `0.1222` n `8`; equity avg `0.1596` n `128`; fx avg `0.0037` n `6`; index avg `0.041` n `26`; metal avg `-0.0287` n `20`; unknown avg `-0.0112` n `791`
- 1h: commodity avg `0.1601` n `12`; crypto_alt avg `0.1095` n `231`; crypto_major avg `0.0401` n `8`; equity avg `0.0895` n `128`; fx avg `-0.0395` n `6`; index avg `0.0447` n `26`; metal avg `-0.1203` n `20`; unknown avg `-0.2285` n `779`
- 4h: commodity avg `-0.0411` n `12`; crypto_alt avg `-2.1484` n `231`; crypto_major avg `-2.148` n `8`; equity avg `-1.022` n `128`; fx avg `-0.0258` n `6`; index avg `-0.1861` n `26`; metal avg `-0.1837` n `20`; unknown avg `4.3356` n `779`
- 24h: commodity avg `0.4503` n `12`; crypto_alt avg `-0.604` n `231`; crypto_major avg `-2.0547` n `8`; equity avg `-1.1473` n `128`; fx avg `-0.023` n `6`; index avg `-0.2692` n `26`; metal avg `-0.3578` n `20`; unknown avg `-0.4177` n `757`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0558`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0471`, n `668`, weak_sample_signal
