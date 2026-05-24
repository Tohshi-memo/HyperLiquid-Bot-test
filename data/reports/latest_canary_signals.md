# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T05:52:16.967328+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0014` n `12`; crypto_alt avg `0.1654` n `228`; crypto_major avg `0.3718` n `8`; equity avg `0.1181` n `67`; fx avg `0.0114` n `6`; index avg `0.0022` n `23`; metal avg `0.0385` n `18`; unknown avg `0.1584` n `396`
- 1h: commodity avg `0.0023` n `12`; crypto_alt avg `-0.3098` n `228`; crypto_major avg `0.2642` n `8`; equity avg `0.0622` n `67`; fx avg `-0.0212` n `6`; index avg `0.037` n `23`; metal avg `0.0524` n `18`; unknown avg `0.3534` n `396`
- 4h: commodity avg `-0.1475` n `12`; crypto_alt avg `-0.8061` n `228`; crypto_major avg `0.0992` n `8`; equity avg `0.1321` n `67`; fx avg `0.0053` n `6`; index avg `0.1122` n `23`; metal avg `0.1059` n `18`; unknown avg `-0.5337` n `396`
- 24h: commodity avg `-3.0125` n `12`; crypto_alt avg `1.7454` n `228`; crypto_major avg `2.7468` n `8`; equity avg `2.439` n `67`; fx avg `0.0389` n `6`; index avg `1.2693` n `23`; metal avg `1.2679` n `18`; unknown avg `1.9224` n `376`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
