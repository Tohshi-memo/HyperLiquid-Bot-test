# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T03:22:11.085035+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0068` n `13`; crypto_alt avg `-0.147` n `239`; crypto_major avg `-0.0188` n `8`; equity avg `-0.0562` n `168`; fx avg `0.0028` n `6`; index avg `-0.0051` n `27`; metal avg `-0.004` n `20`; unknown avg `1.5713` n `1263`
- 1h: commodity avg `0.0073` n `13`; crypto_alt avg `-0.4465` n `239`; crypto_major avg `-0.3116` n `8`; equity avg `-0.0008` n `168`; fx avg `0.0018` n `6`; index avg `-0.0014` n `27`; metal avg `0.0171` n `20`; unknown avg `2.5321` n `1259`
- 4h: commodity avg `-0.0518` n `13`; crypto_alt avg `-0.3306` n `239`; crypto_major avg `0.4316` n `8`; equity avg `0.2562` n `168`; fx avg `-0.0007` n `6`; index avg `0.0384` n `27`; metal avg `0.0359` n `20`; unknown avg `4.6009` n `1247`
- 24h: commodity avg `-0.7375` n `13`; crypto_alt avg `-1.6046` n `239`; crypto_major avg `-1.7871` n `8`; equity avg `0.9899` n `168`; fx avg `-0.1765` n `6`; index avg `0.1021` n `27`; metal avg `0.1172` n `20`; unknown avg `282.5386` n `987`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1429`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
