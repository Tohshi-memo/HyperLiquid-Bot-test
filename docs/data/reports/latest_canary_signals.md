# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T17:52:30.917861+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.221` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0236` n `12`; crypto_alt avg `-0.123` n `228`; crypto_major avg `-0.0067` n `8`; equity avg `0.2226` n `74`; fx avg `-0.0064` n `6`; index avg `0.0524` n `23`; metal avg `0.0878` n `18`; unknown avg `-0.3311` n `550`
- 1h: commodity avg `0.1828` n `12`; crypto_alt avg `-0.6051` n `228`; crypto_major avg `-0.5382` n `8`; equity avg `-0.094` n `74`; fx avg `-0.0319` n `6`; index avg `-0.1297` n `23`; metal avg `-0.2938` n `18`; unknown avg `0.0231` n `548`
- 4h: commodity avg `0.6559` n `12`; crypto_alt avg `-1.6637` n `228`; crypto_major avg `-1.5651` n `8`; equity avg `-1.3686` n `74`; fx avg `-0.0728` n `6`; index avg `-0.8885` n `23`; metal avg `-1.1902` n `18`; unknown avg `0.1253` n `547`
- 24h: commodity avg `1.7246` n `12`; crypto_alt avg `-0.9799` n `228`; crypto_major avg `-1.769` n `8`; equity avg `0.0076` n `74`; fx avg `-0.0828` n `6`; index avg `-0.1001` n `23`; metal avg `-1.3926` n `18`; unknown avg `-0.0241` n `537`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
