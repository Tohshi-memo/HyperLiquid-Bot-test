# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T18:37:40.804911+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.6334` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.4043` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.8478` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.046` n `12`; crypto_alt avg `-0.0651` n `228`; crypto_major avg `-0.2141` n `8`; equity avg `-0.1363` n `86`; fx avg `0.0157` n `6`; index avg `-0.0074` n `23`; metal avg `0.0505` n `20`; unknown avg `-0.331` n `764`
- 1h: commodity avg `-0.0144` n `12`; crypto_alt avg `0.9966` n `228`; crypto_major avg `0.652` n `8`; equity avg `0.3461` n `86`; fx avg `0.0199` n `6`; index avg `0.0471` n `23`; metal avg `-0.0809` n `20`; unknown avg `0.2085` n `764`
- 4h: commodity avg `0.0586` n `12`; crypto_alt avg `-2.7856` n `228`; crypto_major avg `-2.5748` n `8`; equity avg `-1.1806` n `86`; fx avg `0.0503` n `6`; index avg `-0.1705` n `23`; metal avg `-0.727` n `20`; unknown avg `-0.8627` n `764`
- 24h: commodity avg `-0.4992` n `12`; crypto_alt avg `-3.7596` n `228`; crypto_major avg `-3.5441` n `8`; equity avg `2.062` n `86`; fx avg `0.083` n `6`; index avg `0.0233` n `23`; metal avg `-1.948` n `20`; unknown avg `-0.623` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
