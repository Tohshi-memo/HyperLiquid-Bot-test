# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T01:52:28.153517+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0226` n `12`; crypto_alt avg `-0.0068` n `228`; crypto_major avg `-0.003` n `8`; equity avg `-0.0382` n `78`; fx avg `-0.0012` n `6`; index avg `0.002` n `23`; metal avg `-0.0034` n `18`; unknown avg `0.0991` n `687`
- 1h: commodity avg `0.053` n `12`; crypto_alt avg `-0.1437` n `228`; crypto_major avg `0.1089` n `8`; equity avg `-0.0584` n `78`; fx avg `0.008` n `6`; index avg `-0.0038` n `23`; metal avg `-0.046` n `18`; unknown avg `-0.5958` n `679`
- 4h: commodity avg `-0.2871` n `12`; crypto_alt avg `0.5204` n `228`; crypto_major avg `0.5549` n `8`; equity avg `0.2126` n `78`; fx avg `0.0823` n `6`; index avg `0.0618` n `23`; metal avg `-0.0211` n `18`; unknown avg `-0.4969` n `671`
- 24h: commodity avg `0.2839` n `12`; crypto_alt avg `-3.4294` n `228`; crypto_major avg `-4.3054` n `8`; equity avg `0.8674` n `78`; fx avg `-0.0852` n `6`; index avg `0.2702` n `23`; metal avg `-4.1344` n `18`; unknown avg `-0.6276` n `556`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
