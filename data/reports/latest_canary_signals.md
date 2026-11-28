# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T05:22:26.944356+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0046` n `13`; crypto_alt avg `-0.0168` n `239`; crypto_major avg `-0.0038` n `8`; equity avg `-0.057` n `168`; fx avg `0.0` n `6`; index avg `-0.0041` n `27`; metal avg `0.0016` n `20`; unknown avg `4.8579` n `1265`
- 1h: commodity avg `0.0082` n `13`; crypto_alt avg `-1.0142` n `239`; crypto_major avg `-0.606` n `8`; equity avg `-0.2185` n `168`; fx avg `0.0098` n `6`; index avg `-0.0234` n `27`; metal avg `-0.0195` n `20`; unknown avg `0.1359` n `1255`
- 4h: commodity avg `0.0365` n `13`; crypto_alt avg `-1.6016` n `239`; crypto_major avg `-0.8297` n `8`; equity avg `-0.1046` n `168`; fx avg `0.0067` n `6`; index avg `-0.0207` n `27`; metal avg `-0.0026` n `20`; unknown avg `1.4845` n `1243`
- 24h: commodity avg `-0.9172` n `13`; crypto_alt avg `-2.5288` n `239`; crypto_major avg `-2.5527` n `8`; equity avg `-0.2508` n `168`; fx avg `-0.1431` n `6`; index avg `0.0078` n `27`; metal avg `-0.059` n `20`; unknown avg `215.2308` n `977`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
