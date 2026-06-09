# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T02:52:24.155351+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.7427` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.7197` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.6845` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0481` n `12`; crypto_alt avg `-0.087` n `228`; crypto_major avg `0.0065` n `8`; equity avg `0.0028` n `74`; fx avg `0.0084` n `6`; index avg `-0.0118` n `23`; metal avg `0.0914` n `18`; unknown avg `-0.338` n `517`
- 1h: commodity avg `-0.0655` n `12`; crypto_alt avg `-0.8991` n `228`; crypto_major avg `-0.3961` n `8`; equity avg `-0.0311` n `74`; fx avg `0.01` n `6`; index avg `-0.06` n `23`; metal avg `-0.0769` n `18`; unknown avg `-0.2925` n `517`
- 4h: commodity avg `-0.1843` n `12`; crypto_alt avg `-2.5147` n `228`; crypto_major avg `-1.7466` n `8`; equity avg `-0.0039` n `74`; fx avg `-0.0637` n `6`; index avg `-0.0269` n `23`; metal avg `-0.0621` n `18`; unknown avg `0.1315` n `517`
- 24h: commodity avg `-1.0047` n `12`; crypto_alt avg `-1.4117` n `228`; crypto_major avg `-0.7369` n `8`; equity avg `0.8613` n `74`; fx avg `-0.3027` n `6`; index avg `0.5145` n `23`; metal avg `0.087` n `18`; unknown avg `-3.3707` n `507`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
