# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T06:52:25.516982+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0055` n `13`; crypto_alt avg `-0.3393` n `239`; crypto_major avg `-0.331` n `8`; equity avg `-0.0535` n `168`; fx avg `0.0078` n `6`; index avg `-0.0064` n `27`; metal avg `-0.0057` n `20`; unknown avg `176.8639` n `1265`
- 1h: commodity avg `-0.3049` n `13`; crypto_alt avg `-0.577` n `239`; crypto_major avg `-0.7063` n `8`; equity avg `-0.5063` n `168`; fx avg `0.0072` n `6`; index avg `-0.0777` n `27`; metal avg `-0.1881` n `20`; unknown avg `-0.1665` n `1239`
- 4h: commodity avg `-0.1881` n `13`; crypto_alt avg `-0.6339` n `239`; crypto_major avg `-0.663` n `8`; equity avg `-0.5622` n `168`; fx avg `0.008` n `6`; index avg `-0.0594` n `27`; metal avg `-0.2769` n `20`; unknown avg `164.259` n `1221`
- 24h: commodity avg `0.5335` n `13`; crypto_alt avg `2.1598` n `239`; crypto_major avg `2.113` n `8`; equity avg `2.183` n `168`; fx avg `0.0484` n `6`; index avg `0.1425` n `27`; metal avg `0.6517` n `20`; unknown avg `760.0528` n `1031`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
