# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T02:37:27.568120+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.059` n `12`; crypto_alt avg `0.4809` n `234`; crypto_major avg `0.4362` n `8`; equity avg `0.2095` n `137`; fx avg `-0.0023` n `6`; index avg `0.0198` n `27`; metal avg `0.0049` n `20`; unknown avg `0.7919` n `920`
- 1h: commodity avg `-0.0615` n `12`; crypto_alt avg `-0.307` n `234`; crypto_major avg `-0.3019` n `8`; equity avg `-0.1897` n `137`; fx avg `0.0309` n `6`; index avg `-0.0449` n `27`; metal avg `-0.1855` n `20`; unknown avg `0.9175` n `917`
- 4h: commodity avg `0.0038` n `12`; crypto_alt avg `1.7689` n `234`; crypto_major avg `1.1074` n `8`; equity avg `0.4132` n `137`; fx avg `0.0299` n `6`; index avg `0.0739` n `27`; metal avg `0.1746` n `20`; unknown avg `0.7816` n `901`
- 24h: commodity avg `-0.4833` n `12`; crypto_alt avg `1.876` n `234`; crypto_major avg `1.0357` n `8`; equity avg `1.3938` n `137`; fx avg `0.0337` n `6`; index avg `0.1222` n `27`; metal avg `-0.2405` n `20`; unknown avg `0.9708` n `715`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
