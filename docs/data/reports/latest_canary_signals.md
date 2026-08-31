# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T00:22:28.344988+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.2137` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.0703` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-2.0456` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0443` n `12`; crypto_alt avg `0.5859` n `231`; crypto_major avg `0.6087` n `8`; equity avg `0.4933` n `128`; fx avg `0.001` n `6`; index avg `0.1155` n `26`; metal avg `0.0387` n `20`; unknown avg `0.5515` n `793`
- 1h: commodity avg `-0.1318` n `12`; crypto_alt avg `-0.9862` n `231`; crypto_major avg `-0.7028` n `8`; equity avg `-0.2605` n `128`; fx avg `0.0142` n `6`; index avg `-0.1069` n `26`; metal avg `-0.0479` n `20`; unknown avg `2.0038` n `791`
- 4h: commodity avg `-0.3105` n `12`; crypto_alt avg `-2.409` n `231`; crypto_major avg `-2.3561` n `8`; equity avg `-1.0457` n `128`; fx avg `0.0193` n `6`; index avg `-0.2858` n `26`; metal avg `-0.1424` n `20`; unknown avg `2.5485` n `789`
- 24h: commodity avg `0.1298` n `12`; crypto_alt avg `-1.041` n `231`; crypto_major avg `-1.8117` n `8`; equity avg `-0.9536` n `128`; fx avg `0.029` n `6`; index avg `-0.272` n `26`; metal avg `-0.1021` n `20`; unknown avg `-0.399` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0517`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0496`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0489`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0485`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0445`, n `668`, weak_sample_signal
