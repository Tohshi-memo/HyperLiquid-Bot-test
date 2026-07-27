# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T10:22:29.238865+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0501` n `12`; crypto_alt avg `0.0787` n `230`; crypto_major avg `0.1458` n `8`; equity avg `-0.0596` n `100`; fx avg `-0.001` n `6`; index avg `-0.0072` n `25`; metal avg `-0.0142` n `20`; unknown avg `0.0138` n `775`
- 1h: commodity avg `-0.0038` n `12`; crypto_alt avg `0.3199` n `230`; crypto_major avg `0.307` n `8`; equity avg `0.0945` n `100`; fx avg `-0.0062` n `6`; index avg `0.0055` n `25`; metal avg `0.0002` n `20`; unknown avg `0.0473` n `775`
- 4h: commodity avg `-0.2655` n `12`; crypto_alt avg `-0.3705` n `230`; crypto_major avg `-0.1215` n `8`; equity avg `0.2718` n `100`; fx avg `-0.0282` n `6`; index avg `0.0196` n `25`; metal avg `0.0836` n `20`; unknown avg `-0.0684` n `775`
- 24h: commodity avg `-0.6872` n `12`; crypto_alt avg `0.6155` n `230`; crypto_major avg `1.3243` n `8`; equity avg `1.4178` n `100`; fx avg `0.1` n `6`; index avg `0.1563` n `25`; metal avg `0.4008` n `20`; unknown avg `-0.057` n `759`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1961`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
