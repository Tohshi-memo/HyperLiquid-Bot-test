# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T00:22:23.086400+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0029` n `13`; crypto_alt avg `-0.0003` n `239`; crypto_major avg `0.1197` n `8`; equity avg `0.0568` n `166`; fx avg `-0.0187` n `6`; index avg `0.0039` n `27`; metal avg `0.0125` n `20`; unknown avg `0.02` n `1261`
- 1h: commodity avg `0.0416` n `13`; crypto_alt avg `0.1535` n `239`; crypto_major avg `0.2` n `8`; equity avg `0.5082` n `166`; fx avg `-0.0553` n `6`; index avg `0.1367` n `27`; metal avg `-0.0909` n `20`; unknown avg `319.0262` n `1252`
- 4h: commodity avg `-0.3685` n `13`; crypto_alt avg `0.0885` n `239`; crypto_major avg `0.6593` n `8`; equity avg `0.7569` n `166`; fx avg `0.0601` n `6`; index avg `0.1266` n `27`; metal avg `0.2742` n `20`; unknown avg `166.4003` n `1202`
- 24h: commodity avg `-0.4608` n `13`; crypto_alt avg `0.5981` n `239`; crypto_major avg `1.0103` n `8`; equity avg `1.4457` n `166`; fx avg `0.0567` n `6`; index avg `0.1832` n `27`; metal avg `0.3039` n `20`; unknown avg `435.3385` n `1035`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1746`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1736`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1734`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1594`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1526`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
