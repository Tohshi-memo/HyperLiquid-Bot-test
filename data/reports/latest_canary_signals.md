# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T01:37:16.460062+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1477` n `12`; crypto_alt avg `0.284` n `228`; crypto_major avg `0.1367` n `8`; equity avg `0.0339` n `67`; fx avg `0.0007` n `6`; index avg `0.0059` n `23`; metal avg `0.0229` n `18`; unknown avg `-0.092` n `386`
- 1h: commodity avg `0.1395` n `12`; crypto_alt avg `0.8222` n `228`; crypto_major avg `0.4747` n `8`; equity avg `0.1719` n `67`; fx avg `-0.0012` n `6`; index avg `0.0598` n `23`; metal avg `-0.0078` n `18`; unknown avg `-0.5114` n `386`
- 4h: commodity avg `0.712` n `12`; crypto_alt avg `-1.0424` n `228`; crypto_major avg `-0.8068` n `8`; equity avg `-0.5654` n `67`; fx avg `0.0021` n `6`; index avg `-0.2076` n `23`; metal avg `-0.1239` n `18`; unknown avg `-0.9954` n `386`
- 24h: commodity avg `-0.0282` n `12`; crypto_alt avg `-2.9584` n `228`; crypto_major avg `-2.1402` n `8`; equity avg `-1.6119` n `67`; fx avg `0.096` n `6`; index avg `0.0307` n `23`; metal avg `-0.6946` n `18`; unknown avg `-2.0868` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0512`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0489`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0478`, n `668`, weak_sample_signal
