# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T14:37:35.896444+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0602` n `12`; crypto_alt avg `-0.2669` n `232`; crypto_major avg `-0.3057` n `8`; equity avg `-0.0364` n `133`; fx avg `-0.0093` n `6`; index avg `0.0042` n `26`; metal avg `-0.0632` n `20`; unknown avg `0.4472` n `791`
- 1h: commodity avg `0.1531` n `12`; crypto_alt avg `0.5118` n `232`; crypto_major avg `0.7197` n `8`; equity avg `0.5608` n `133`; fx avg `-0.0152` n `6`; index avg `0.1194` n `26`; metal avg `0.0507` n `20`; unknown avg `0.8997` n `789`
- 4h: commodity avg `-0.0299` n `12`; crypto_alt avg `0.4832` n `232`; crypto_major avg `0.8415` n `8`; equity avg `1.2251` n `133`; fx avg `-0.1407` n `6`; index avg `0.2719` n `26`; metal avg `0.633` n `20`; unknown avg `1.0955` n `789`
- 24h: commodity avg `0.6985` n `12`; crypto_alt avg `-1.5072` n `232`; crypto_major avg `-1.8481` n `8`; equity avg `-0.1953` n `132`; fx avg `-0.3532` n `6`; index avg `-0.059` n `26`; metal avg `0.1065` n `20`; unknown avg `0.0573` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0515`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0481`, n `668`, weak_sample_signal
