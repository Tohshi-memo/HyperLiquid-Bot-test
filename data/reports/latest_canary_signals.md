# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T17:37:24.743484+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.85` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `-2.5351` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `-2.4251` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.2358` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0004` n `12`; crypto_alt avg `0.2851` n `228`; crypto_major avg `0.0554` n `8`; equity avg `-0.2016` n `69`; fx avg `-0.0043` n `6`; index avg `-0.0818` n `23`; metal avg `-0.0836` n `18`; unknown avg `0.0704` n `422`
- 1h: commodity avg `0.1305` n `12`; crypto_alt avg `0.4397` n `228`; crypto_major avg `-0.0195` n `8`; equity avg `-0.0208` n `69`; fx avg `-0.0291` n `6`; index avg `-0.1343` n `23`; metal avg `-0.1799` n `18`; unknown avg `-0.2734` n `422`
- 4h: commodity avg `0.5599` n `12`; crypto_alt avg `-1.6976` n `228`; crypto_major avg `-1.8652` n `8`; equity avg `0.6699` n `69`; fx avg `-0.0321` n `6`; index avg `0.3706` n `23`; metal avg `-0.4486` n `18`; unknown avg `-0.1737` n `422`
- 24h: commodity avg `0.3141` n `12`; crypto_alt avg `-2.2607` n `228`; crypto_major avg `-3.2133` n `8`; equity avg `-0.0201` n `69`; fx avg `0.091` n `6`; index avg `0.3245` n `23`; metal avg `0.2705` n `18`; unknown avg `0.055` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
