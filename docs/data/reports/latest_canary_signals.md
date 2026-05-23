# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T09:22:17.914081+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0168` n `12`; crypto_alt avg `-0.0059` n `228`; crypto_major avg `-0.0596` n `8`; equity avg `-0.0122` n `67`; fx avg `0.0` n `6`; index avg `0.0045` n `23`; metal avg `0.0035` n `18`; unknown avg `0.0817` n `396`
- 1h: commodity avg `0.015` n `12`; crypto_alt avg `0.1678` n `228`; crypto_major avg `0.0365` n `8`; equity avg `0.0567` n `67`; fx avg `0.0035` n `6`; index avg `-0.0072` n `23`; metal avg `0.0003` n `18`; unknown avg `1.2653` n `386`
- 4h: commodity avg `-0.1288` n `12`; crypto_alt avg `-1.6399` n `228`; crypto_major avg `-1.125` n `8`; equity avg `-0.2424` n `67`; fx avg `-0.0242` n `6`; index avg `-0.1251` n `23`; metal avg `0.0097` n `18`; unknown avg `0.8118` n `376`
- 24h: commodity avg `-0.5086` n `12`; crypto_alt avg `-5.957` n `228`; crypto_major avg `-4.1956` n `8`; equity avg `-1.8421` n `67`; fx avg `0.0329` n `6`; index avg `-0.2187` n `23`; metal avg `-0.3242` n `18`; unknown avg `-1.1312` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0513`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0504`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0482`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0479`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0452`, n `668`, weak_sample_signal
