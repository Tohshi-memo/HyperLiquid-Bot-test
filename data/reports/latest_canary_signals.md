# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T03:52:30.824894+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0038` n `12`; crypto_alt avg `-0.0321` n `230`; crypto_major avg `0.0033` n `8`; equity avg `-0.0164` n `100`; fx avg `-0.005` n `6`; index avg `0.0086` n `25`; metal avg `0.004` n `20`; unknown avg `-0.0345` n `775`
- 1h: commodity avg `-0.0361` n `12`; crypto_alt avg `0.099` n `230`; crypto_major avg `0.0916` n `8`; equity avg `0.061` n `100`; fx avg `-0.0` n `6`; index avg `0.0138` n `25`; metal avg `0.0072` n `20`; unknown avg `0.1563` n `774`
- 4h: commodity avg `-0.0173` n `12`; crypto_alt avg `0.4635` n `230`; crypto_major avg `0.4887` n `8`; equity avg `0.1887` n `100`; fx avg `-0.0101` n `6`; index avg `0.0385` n `25`; metal avg `0.0206` n `20`; unknown avg `-0.1861` n `774`
- 24h: commodity avg `-0.4711` n `12`; crypto_alt avg `0.9152` n `230`; crypto_major avg `1.4323` n `8`; equity avg `0.4868` n `100`; fx avg `-0.0011` n `6`; index avg `0.1497` n `25`; metal avg `0.0478` n `20`; unknown avg `-0.2124` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1831`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1725`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1544`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1375`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1245`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1219`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1177`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1164`, n `666`, weak_sample_signal
