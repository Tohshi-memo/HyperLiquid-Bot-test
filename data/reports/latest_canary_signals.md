# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T04:37:20.306422+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0164` n `12`; crypto_alt avg `-0.0137` n `228`; crypto_major avg `-0.0636` n `8`; equity avg `0.0153` n `67`; fx avg `0.0115` n `6`; index avg `-0.0202` n `23`; metal avg `0.0003` n `18`; unknown avg `-0.1268` n `396`
- 1h: commodity avg `-0.0444` n `12`; crypto_alt avg `0.0548` n `228`; crypto_major avg `-0.0983` n `8`; equity avg `0.0157` n `67`; fx avg `0.0102` n `6`; index avg `-0.0311` n `23`; metal avg `-0.0463` n `18`; unknown avg `-0.4689` n `396`
- 4h: commodity avg `-0.1179` n `12`; crypto_alt avg `-0.3847` n `228`; crypto_major avg `0.0624` n `8`; equity avg `0.2426` n `67`; fx avg `0.0118` n `6`; index avg `0.2109` n `23`; metal avg `0.1908` n `18`; unknown avg `-0.4683` n `396`
- 24h: commodity avg `-3.064` n `12`; crypto_alt avg `1.785` n `228`; crypto_major avg `2.2512` n `8`; equity avg `2.2026` n `67`; fx avg `0.0478` n `6`; index avg `1.1251` n `23`; metal avg `1.1592` n `18`; unknown avg `1.5451` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
