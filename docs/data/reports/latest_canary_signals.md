# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T14:37:35.533776+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0044` n `13`; crypto_alt avg `-0.1625` n `235`; crypto_major avg `-0.0835` n `8`; equity avg `-0.068` n `150`; fx avg `0.0061` n `6`; index avg `0.0085` n `26`; metal avg `0.0597` n `20`; unknown avg `-0.1407` n `1076`
- 1h: commodity avg `-0.1249` n `13`; crypto_alt avg `-0.0974` n `235`; crypto_major avg `-0.0387` n `8`; equity avg `0.2699` n `150`; fx avg `-0.0029` n `6`; index avg `0.0371` n `26`; metal avg `0.1602` n `20`; unknown avg `0.3995` n `1028`
- 4h: commodity avg `0.1081` n `13`; crypto_alt avg `-1.1063` n `235`; crypto_major avg `-0.7401` n `8`; equity avg `-0.451` n `150`; fx avg `-0.0382` n `6`; index avg `-0.137` n `26`; metal avg `-0.1556` n `20`; unknown avg `0.1635` n `1022`
- 24h: commodity avg `1.1624` n `13`; crypto_alt avg `-5.8998` n `235`; crypto_major avg `-4.1977` n `8`; equity avg `-1.7206` n `150`; fx avg `-0.1578` n `6`; index avg `-0.3836` n `26`; metal avg `-0.506` n `20`; unknown avg `17.0267` n `980`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
