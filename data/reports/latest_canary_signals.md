# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T12:52:27.038265+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0018` n `12`; crypto_alt avg `0.1429` n `230`; crypto_major avg `0.0871` n `8`; equity avg `0.0129` n `100`; fx avg `-0.0005` n `6`; index avg `0.0015` n `25`; metal avg `-0.0012` n `20`; unknown avg `0.0081` n `774`
- 1h: commodity avg `0.0114` n `12`; crypto_alt avg `0.1918` n `230`; crypto_major avg `0.0341` n `8`; equity avg `0.0403` n `100`; fx avg `-0.0016` n `6`; index avg `0.0028` n `25`; metal avg `-0.0011` n `20`; unknown avg `0.0172` n `774`
- 4h: commodity avg `-0.0611` n `12`; crypto_alt avg `0.372` n `230`; crypto_major avg `0.3773` n `8`; equity avg `0.0455` n `100`; fx avg `-0.031` n `6`; index avg `0.0057` n `25`; metal avg `-0.002` n `20`; unknown avg `0.3992` n `774`
- 24h: commodity avg `-0.1901` n `12`; crypto_alt avg `-0.8545` n `230`; crypto_major avg `-0.6362` n `8`; equity avg `-2.7863` n `100`; fx avg `-0.0062` n `6`; index avg `-0.2407` n `25`; metal avg `-0.1231` n `20`; unknown avg `13.1868` n `757`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1613`, n `669`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.153`, n `669`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1236`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1204`, n `667`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1176`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.114`, n `667`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1118`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1112`, n `669`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.104`, n `667`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1022`, n `669`, weak_sample_signal
