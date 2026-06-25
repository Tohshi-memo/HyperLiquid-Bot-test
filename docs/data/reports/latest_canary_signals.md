# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T17:22:44.815649+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.3095` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.073` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.8087` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0501` n `12`; crypto_alt avg `0.7644` n `228`; crypto_major avg `0.9397` n `8`; equity avg `0.0766` n `86`; fx avg `0.0011` n `6`; index avg `0.0064` n `23`; metal avg `0.0088` n `20`; unknown avg `0.2825` n `765`
- 1h: commodity avg `-0.0249` n `12`; crypto_alt avg `-0.2233` n `228`; crypto_major avg `0.1159` n `8`; equity avg `-0.4374` n `86`; fx avg `-0.0066` n `6`; index avg `-0.072` n `23`; metal avg `-0.1397` n `20`; unknown avg `-0.0219` n `765`
- 4h: commodity avg `0.2327` n `12`; crypto_alt avg `-1.8734` n `228`; crypto_major avg `-2.0768` n `8`; equity avg `-2.5837` n `86`; fx avg `0.0601` n `6`; index avg `-0.2681` n `23`; metal avg `-0.0038` n `20`; unknown avg `1.0663` n `765`
- 24h: commodity avg `0.3757` n `12`; crypto_alt avg `1.955` n `228`; crypto_major avg `1.2834` n `8`; equity avg `0.2288` n `86`; fx avg `0.0648` n `6`; index avg `0.4397` n `23`; metal avg `0.516` n `20`; unknown avg `0.5507` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1581`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
