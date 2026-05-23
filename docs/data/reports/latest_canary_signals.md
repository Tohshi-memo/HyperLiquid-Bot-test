# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T18:52:13.457440+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1011` n `12`; crypto_alt avg `-0.1484` n `228`; crypto_major avg `-0.0767` n `8`; equity avg `-0.0863` n `67`; fx avg `0.0006` n `6`; index avg `-0.1317` n `23`; metal avg `0.0001` n `18`; unknown avg `0.9365` n `396`
- 1h: commodity avg `-0.6629` n `12`; crypto_alt avg `0.9721` n `228`; crypto_major avg `0.7645` n `8`; equity avg `0.5081` n `67`; fx avg `0.0004` n `6`; index avg `0.3216` n `23`; metal avg `0.0909` n `18`; unknown avg `2.0641` n `396`
- 4h: commodity avg `-0.4784` n `12`; crypto_alt avg `1.9339` n `228`; crypto_major avg `1.3142` n `8`; equity avg `0.631` n `67`; fx avg `0.005` n `6`; index avg `0.1662` n `23`; metal avg `0.2292` n `18`; unknown avg `1.8903` n `396`
- 24h: commodity avg `-0.2856` n `12`; crypto_alt avg `-0.1453` n `228`; crypto_major avg `-0.2131` n `8`; equity avg `-0.0646` n `67`; fx avg `0.0097` n `6`; index avg `0.0465` n `23`; metal avg `-0.0617` n `18`; unknown avg `-0.2595` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
