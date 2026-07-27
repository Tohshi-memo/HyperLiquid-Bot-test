# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T11:52:30.642072+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0211` n `12`; crypto_alt avg `-0.1001` n `230`; crypto_major avg `-0.0755` n `8`; equity avg `0.0474` n `100`; fx avg `-0.0053` n `6`; index avg `-0.0135` n `25`; metal avg `-0.0385` n `20`; unknown avg `-0.008` n `776`
- 1h: commodity avg `0.0331` n `12`; crypto_alt avg `-0.1734` n `230`; crypto_major avg `-0.2748` n `8`; equity avg `-0.3817` n `100`; fx avg `-0.0063` n `6`; index avg `-0.0682` n `25`; metal avg `-0.0729` n `20`; unknown avg `-0.0361` n `776`
- 4h: commodity avg `-0.1597` n `12`; crypto_alt avg `-0.3039` n `230`; crypto_major avg `-0.2065` n `8`; equity avg `-0.2455` n `100`; fx avg `-0.0241` n `6`; index avg `-0.026` n `25`; metal avg `-0.0001` n `20`; unknown avg `-0.1325` n `775`
- 24h: commodity avg `-0.5838` n `12`; crypto_alt avg `0.4539` n `230`; crypto_major avg `1.1515` n `8`; equity avg `0.8537` n `100`; fx avg `0.0899` n `6`; index avg `0.0902` n `25`; metal avg `0.3218` n `20`; unknown avg `-0.1609` n `759`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.2002`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
