# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T17:07:25.668541+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1215` n `12`; crypto_alt avg `-0.4307` n `228`; crypto_major avg `-0.2854` n `8`; equity avg `-0.2067` n `67`; fx avg `0.026` n `6`; index avg `-0.2027` n `23`; metal avg `-0.1681` n `18`; unknown avg `-0.0577` n `418`
- 1h: commodity avg `-0.1043` n `12`; crypto_alt avg `-0.8497` n `228`; crypto_major avg `-0.4596` n `8`; equity avg `0.0321` n `67`; fx avg `0.0359` n `6`; index avg `0.0706` n `23`; metal avg `0.0694` n `18`; unknown avg `-0.3362` n `418`
- 4h: commodity avg `0.6951` n `12`; crypto_alt avg `-0.1433` n `228`; crypto_major avg `-0.5255` n `8`; equity avg `-0.8646` n `67`; fx avg `-0.0041` n `6`; index avg `-0.832` n `23`; metal avg `0.201` n `18`; unknown avg `-0.3643` n `418`
- 24h: commodity avg `-1.0487` n `12`; crypto_alt avg `-1.3485` n `228`; crypto_major avg `-1.0303` n `8`; equity avg `-0.5639` n `67`; fx avg `-0.0478` n `6`; index avg `-0.5727` n `23`; metal avg `-0.9763` n `18`; unknown avg `-0.7396` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1723`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.17`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1613`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1533`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
