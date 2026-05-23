# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T08:22:16.174076+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2236` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0281` n `12`; crypto_alt avg `0.4773` n `228`; crypto_major avg `0.2345` n `8`; equity avg `0.1269` n `67`; fx avg `-0.0126` n `6`; index avg `0.0227` n `23`; metal avg `0.0358` n `18`; unknown avg `-0.2084` n `386`
- 1h: commodity avg `0.0106` n `12`; crypto_alt avg `-1.785` n `228`; crypto_major avg `-0.9615` n `8`; equity avg `-0.2915` n `67`; fx avg `-0.0382` n `6`; index avg `-0.0568` n `23`; metal avg `-0.0658` n `18`; unknown avg `-0.2799` n `386`
- 4h: commodity avg `-0.1264` n `12`; crypto_alt avg `-2.1492` n `228`; crypto_major avg `-1.4247` n `8`; equity avg `-0.4205` n `67`; fx avg `-0.0215` n `6`; index avg `-0.2011` n `23`; metal avg `-0.0264` n `18`; unknown avg `-0.7` n `376`
- 24h: commodity avg `-0.4858` n `12`; crypto_alt avg `-6.1411` n `228`; crypto_major avg `-4.0433` n `8`; equity avg `-2.4375` n `67`; fx avg `0.0068` n `6`; index avg `-0.3606` n `23`; metal avg `-0.677` n `18`; unknown avg `-2.7262` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0529`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0517`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0464`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0464`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0457`, n `668`, weak_sample_signal
