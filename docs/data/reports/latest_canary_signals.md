# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T12:52:28.245331+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2056` n `12`; crypto_alt avg `0.0581` n `228`; crypto_major avg `0.0314` n `8`; equity avg `0.2055` n `74`; fx avg `-0.0106` n `6`; index avg `0.0199` n `23`; metal avg `-0.2734` n `18`; unknown avg `-0.2521` n `424`
- 1h: commodity avg `-0.0801` n `12`; crypto_alt avg `-0.59` n `228`; crypto_major avg `-0.4298` n `8`; equity avg `-0.3359` n `74`; fx avg `-0.0705` n `6`; index avg `-0.2309` n `23`; metal avg `-0.6771` n `18`; unknown avg `-0.2916` n `424`
- 4h: commodity avg `-0.2847` n `12`; crypto_alt avg `-0.0075` n `228`; crypto_major avg `-0.0483` n `8`; equity avg `-0.1436` n `74`; fx avg `-0.0174` n `6`; index avg `-0.1933` n `23`; metal avg `-0.2012` n `18`; unknown avg `1.0732` n `424`
- 24h: commodity avg `-0.4049` n `12`; crypto_alt avg `-6.6594` n `228`; crypto_major avg `-4.9455` n `8`; equity avg `-1.1571` n `74`; fx avg `0.0672` n `6`; index avg `-0.282` n `23`; metal avg `-1.5693` n `18`; unknown avg `-0.5607` n `404`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
