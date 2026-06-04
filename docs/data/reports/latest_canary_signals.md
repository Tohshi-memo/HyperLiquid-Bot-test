# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T02:07:22.511066+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-4.6586` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `4.1274` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-3.7794` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-3.4956` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `-2.3766` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `2.2777` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_commodity_crypto_divergence: score `-2.2515` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_equity_divergence: score `-1.7931` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.025` n `12`; crypto_alt avg `-1.86` n `228`; crypto_major avg `-0.4475` n `8`; equity avg `-0.0292` n `73`; fx avg `0.0028` n `6`; index avg `-0.1208` n `23`; metal avg `0.2094` n `18`; unknown avg `-0.2249` n `420`
- 1h: commodity avg `-0.2491` n `12`; crypto_alt avg `-4.4376` n `228`; crypto_major avg `-2.5006` n `8`; equity avg `-0.7075` n `73`; fx avg `0.0234` n `6`; index avg `-0.2229` n `23`; metal avg `-0.124` n `18`; unknown avg `-1.0027` n `420`
- 4h: commodity avg `-0.53` n `12`; crypto_alt avg `-6.3729` n `228`; crypto_major avg `-4.3094` n `8`; equity avg `-0.8138` n `73`; fx avg `0.0054` n `6`; index avg `-0.182` n `23`; metal avg `0.3492` n `18`; unknown avg `-1.043` n `419`
- 24h: commodity avg `-0.0682` n `12`; crypto_alt avg `-4.3217` n `228`; crypto_major avg `-4.3778` n `8`; equity avg `-3.9334` n `72`; fx avg `0.0364` n `6`; index avg `-1.3182` n `23`; metal avg `-1.6118` n `18`; unknown avg `-0.1245` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1668`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
