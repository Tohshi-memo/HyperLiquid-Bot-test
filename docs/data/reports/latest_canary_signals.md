# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T16:52:27.942367+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.22` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `-2.8917` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-2.6305` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `2.5145` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.5923` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0373` n `12`; crypto_alt avg `-0.1661` n `228`; crypto_major avg `-0.2731` n `8`; equity avg `0.2786` n `69`; fx avg `-0.0122` n `6`; index avg `-0.0352` n `23`; metal avg `0.0516` n `18`; unknown avg `-0.2034` n `422`
- 1h: commodity avg `0.1483` n `12`; crypto_alt avg `1.5124` n `228`; crypto_major avg `0.6154` n `8`; equity avg `0.3234` n `69`; fx avg `-0.014` n `6`; index avg `-0.0759` n `23`; metal avg `-0.3147` n `18`; unknown avg `1.4361` n `422`
- 4h: commodity avg `0.7481` n `12`; crypto_alt avg `-2.0689` n `228`; crypto_major avg `-2.1436` n `8`; equity avg `0.4869` n `69`; fx avg `-0.0087` n `6`; index avg `0.3709` n `23`; metal avg `-0.5513` n `18`; unknown avg `-0.158` n `422`
- 24h: commodity avg `-0.6692` n `12`; crypto_alt avg `-2.3948` n `228`; crypto_major avg `-2.9051` n `8`; equity avg `0.6761` n `69`; fx avg `0.1227` n `6`; index avg `0.5812` n `23`; metal avg `0.642` n `18`; unknown avg `-0.1558` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
