# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T07:07:24.116663+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-3.2508` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.9113` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-2.7274` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-2.3532` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `-2.2892` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.8197` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1701` n `12`; crypto_alt avg `-0.5962` n `228`; crypto_major avg `-0.6391` n `8`; equity avg `-0.2316` n `74`; fx avg `0.0186` n `6`; index avg `-0.1311` n `23`; metal avg `-0.0675` n `18`; unknown avg `0.3` n `424`
- 1h: commodity avg `-0.2703` n `12`; crypto_alt avg `-2.783` n `228`; crypto_major avg `-2.0329` n `8`; equity avg `-0.7078` n `74`; fx avg `0.0106` n `6`; index avg `-0.2132` n `23`; metal avg `0.2563` n `18`; unknown avg `-0.3248` n `424`
- 4h: commodity avg `-0.3567` n `12`; crypto_alt avg `-3.3124` n `228`; crypto_major avg `-3.0841` n `8`; equity avg `-0.7309` n `74`; fx avg `-0.0217` n `6`; index avg `-0.1728` n `23`; metal avg `0.1667` n `18`; unknown avg `-0.5485` n `404`
- 24h: commodity avg `-0.3623` n `12`; crypto_alt avg `-7.9566` n `228`; crypto_major avg `-6.3588` n `8`; equity avg `-2.2414` n `73`; fx avg `0.1349` n `6`; index avg `-0.7242` n `23`; metal avg `-0.3794` n `18`; unknown avg `-1.5156` n `402`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
