# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T02:07:20.316126+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0571` n `12`; crypto_alt avg `0.177` n `228`; crypto_major avg `0.0141` n `8`; equity avg `-0.0723` n `67`; fx avg `-0.0013` n `6`; index avg `0.0186` n `23`; metal avg `-0.0018` n `18`; unknown avg `0.245` n `386`
- 1h: commodity avg `0.0248` n `12`; crypto_alt avg `0.355` n `228`; crypto_major avg `-0.054` n `8`; equity avg `0.0489` n `67`; fx avg `-0.0006` n `6`; index avg `0.0421` n `23`; metal avg `0.0199` n `18`; unknown avg `-0.3218` n `386`
- 4h: commodity avg `0.5779` n `12`; crypto_alt avg `-0.8082` n `228`; crypto_major avg `-0.8673` n `8`; equity avg `-0.5415` n `67`; fx avg `-0.0024` n `6`; index avg `-0.1193` n `23`; metal avg `-0.1429` n `18`; unknown avg `-0.947` n `386`
- 24h: commodity avg `0.0421` n `12`; crypto_alt avg `-3.3822` n `228`; crypto_major avg `-2.7407` n `8`; equity avg `-1.6618` n `67`; fx avg `0.0914` n `6`; index avg `0.0535` n `23`; metal avg `-0.7908` n `18`; unknown avg `-1.8585` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0521`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0509`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0488`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0476`, n `668`, weak_sample_signal
