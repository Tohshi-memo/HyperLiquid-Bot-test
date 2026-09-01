# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T18:22:35.648514+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0275` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.3567` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0452` n `12`; crypto_alt avg `-0.368` n `232`; crypto_major avg `-0.2879` n `8`; equity avg `-0.0952` n `131`; fx avg `-0.0014` n `6`; index avg `-0.0098` n `26`; metal avg `-0.0098` n `20`; unknown avg `-0.2806` n `793`
- 1h: commodity avg `0.0476` n `12`; crypto_alt avg `-0.8119` n `232`; crypto_major avg `-0.7938` n `8`; equity avg `-0.1351` n `131`; fx avg `0.0074` n `6`; index avg `-0.0305` n `26`; metal avg `-0.0937` n `20`; unknown avg `-0.9502` n `791`
- 4h: commodity avg `0.5323` n `12`; crypto_alt avg `-1.4654` n `232`; crypto_major avg `-1.4952` n `8`; equity avg `-0.3252` n `131`; fx avg `-0.0005` n `6`; index avg `-0.1385` n `26`; metal avg `-0.2727` n `20`; unknown avg `-1.3152` n `790`
- 24h: commodity avg `0.6938` n `12`; crypto_alt avg `-0.8413` n `232`; crypto_major avg `-2.1991` n `8`; equity avg `-1.6337` n `130`; fx avg `0.0405` n `6`; index avg `-0.2946` n `26`; metal avg `-0.7059` n `20`; unknown avg `-0.2122` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0487`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0381`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0374`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0373`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0357`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0354`, n `668`, weak_sample_signal
