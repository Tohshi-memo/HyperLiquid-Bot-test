# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T15:52:22.831347+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.21` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `3.2953` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-3.0846` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-2.9449` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `-2.5431` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.6765` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-1.6462` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `-1.5049` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.2662` n `12`; crypto_alt avg `0.4681` n `228`; crypto_major avg `0.3113` n `8`; equity avg `0.0673` n `69`; fx avg `0.0108` n `6`; index avg `0.0139` n `23`; metal avg `-0.0701` n `18`; unknown avg `0.0989` n `422`
- 1h: commodity avg `0.2582` n `12`; crypto_alt avg `-1.9212` n `228`; crypto_major avg `-1.4723` n `8`; equity avg `0.0326` n `69`; fx avg `-0.0025` n `6`; index avg `0.2042` n `23`; metal avg `0.1739` n `18`; unknown avg `-0.8008` n `422`
- 4h: commodity avg `0.2541` n `12`; crypto_alt avg `-3.4518` n `228`; crypto_major avg `-2.8305` n `8`; equity avg `0.1144` n `69`; fx avg `-0.0061` n `6`; index avg `0.4648` n `23`; metal avg `-0.2874` n `18`; unknown avg `-0.6077` n `422`
- 24h: commodity avg `-0.8102` n `12`; crypto_alt avg `-2.8827` n `228`; crypto_major avg `-2.9622` n `8`; equity avg `0.3788` n `69`; fx avg `0.1611` n `6`; index avg `0.7992` n `23`; metal avg `0.9391` n `18`; unknown avg `-1.0506` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1472`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
