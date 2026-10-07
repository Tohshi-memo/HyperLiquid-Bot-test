# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T09:22:33.261850+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0013` n `13`; crypto_alt avg `-0.1217` n `235`; crypto_major avg `-0.1788` n `8`; equity avg `-0.1225` n `150`; fx avg `-0.0068` n `6`; index avg `-0.014` n `26`; metal avg `-0.0057` n `20`; unknown avg `-0.0745` n `1076`
- 1h: commodity avg `0.0323` n `13`; crypto_alt avg `-0.6572` n `235`; crypto_major avg `-0.4884` n `8`; equity avg `-0.4584` n `150`; fx avg `0.0227` n `6`; index avg `-0.0598` n `26`; metal avg `-0.1761` n `20`; unknown avg `0.0941` n `1074`
- 4h: commodity avg `0.0594` n `13`; crypto_alt avg `-0.4665` n `235`; crypto_major avg `-0.308` n `8`; equity avg `-0.5942` n `150`; fx avg `-0.0892` n `6`; index avg `-0.0898` n `26`; metal avg `-0.2493` n `20`; unknown avg `0.0804` n `1036`
- 24h: commodity avg `1.0183` n `13`; crypto_alt avg `-4.0521` n `235`; crypto_major avg `-2.8512` n `8`; equity avg `-0.9252` n `150`; fx avg `-0.0651` n `6`; index avg `-0.1799` n `26`; metal avg `-0.4517` n `20`; unknown avg `815.3399` n `978`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1789`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1688`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1677`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
