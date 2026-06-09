# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T03:52:20.274969+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.6102` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.4123` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0447` n `12`; crypto_alt avg `0.1415` n `228`; crypto_major avg `0.0086` n `8`; equity avg `0.1569` n `74`; fx avg `0.0011` n `6`; index avg `0.0596` n `23`; metal avg `0.0412` n `18`; unknown avg `-0.1577` n `517`
- 1h: commodity avg `-0.1359` n `12`; crypto_alt avg `0.2486` n `228`; crypto_major avg `0.2152` n `8`; equity avg `0.5179` n `74`; fx avg `0.0071` n `6`; index avg `0.2497` n `23`; metal avg `-0.0115` n `18`; unknown avg `-0.0979` n `517`
- 4h: commodity avg `-0.3054` n `12`; crypto_alt avg `-1.6932` n `228`; crypto_major avg `-1.1679` n `8`; equity avg `0.4423` n `74`; fx avg `-0.0695` n `6`; index avg `0.2444` n `23`; metal avg `0.1712` n `18`; unknown avg `-0.3868` n `517`
- 24h: commodity avg `-1.1128` n `12`; crypto_alt avg `-1.1954` n `228`; crypto_major avg `-0.339` n `8`; equity avg `1.617` n `74`; fx avg `-0.3027` n `6`; index avg `0.7057` n `23`; metal avg `0.14` n `18`; unknown avg `-3.1946` n `507`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
