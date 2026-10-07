# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T15:37:35.887549+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1145` n `13`; crypto_alt avg `0.4627` n `235`; crypto_major avg `0.398` n `8`; equity avg `0.173` n `150`; fx avg `-0.0107` n `6`; index avg `0.039` n `26`; metal avg `0.1193` n `20`; unknown avg `0.5733` n `1076`
- 1h: commodity avg `0.0063` n `13`; crypto_alt avg `0.1966` n `235`; crypto_major avg `0.2225` n `8`; equity avg `0.1563` n `150`; fx avg `-0.0023` n `6`; index avg `0.0681` n `26`; metal avg `0.0871` n `20`; unknown avg `0.9015` n `1074`
- 4h: commodity avg `-0.0581` n `13`; crypto_alt avg `-0.483` n `235`; crypto_major avg `-0.3439` n `8`; equity avg `0.0309` n `150`; fx avg `-0.0187` n `6`; index avg `0.0003` n `26`; metal avg `-0.078` n `20`; unknown avg `-0.1978` n `1022`
- 24h: commodity avg `1.1363` n `13`; crypto_alt avg `-6.0237` n `235`; crypto_major avg `-4.0739` n `8`; equity avg `-1.8433` n `150`; fx avg `-0.19` n `6`; index avg `-0.3663` n `26`; metal avg `-0.5789` n `20`; unknown avg `16.8662` n `988`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1445`, n `669`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.143`, n `669`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1404`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0921`, n `669`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0907`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0775`, n `669`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0771`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0768`, n `669`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0757`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0736`, n `669`, weak_sample_signal
